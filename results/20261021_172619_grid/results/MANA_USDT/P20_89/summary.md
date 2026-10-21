# EMA Hourly Continuation — MANA/USDT P20_89

**Symbol:** MANA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 1.0001 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.0864 |
| sortino_ratio | -0.6618 |
| max_drawdown | 0.5830 |
| cagr | -0.2627 |
| net_avg_win | 78.9898 |
| net_avg_loss | -96.7639 |
| avg_hold_time_bars | 16.2252 |
| exposure | 0.3636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
