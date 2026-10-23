# EMA Hourly Continuation — PEOPLE/USDT P26_89

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 615 |
| net_profit_factor | 0.6019 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -3.8713 |
| sortino_ratio | -1.3493 |
| max_drawdown | 0.8161 |
| cagr | -0.4732 |
| net_avg_win | 42.6648 |
| net_avg_loss | -60.8209 |
| avg_hold_time_bars | 13.1398 |
| exposure | 0.3657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
