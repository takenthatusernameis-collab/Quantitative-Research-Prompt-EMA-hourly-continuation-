# EMA Hourly Continuation — MANA/USDT P26_89

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.8031 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0429 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.6795 |
| sortino_ratio | -0.5102 |
| max_drawdown | 0.5049 |
| cagr | -0.2094 |
| net_avg_win | 80.4131 |
| net_avg_loss | -101.4816 |
| avg_hold_time_bars | 14.7082 |
| exposure | 0.3002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
