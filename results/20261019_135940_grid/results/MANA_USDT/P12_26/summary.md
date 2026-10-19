# EMA Hourly Continuation — MANA/USDT P12_26

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1456 |
| net_profit_factor | 0.3524 |
| net_win_rate | 0.4245 |
| gross_profit_factor | 0.9254 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -12.0046 |
| sortino_ratio | -6.5010 |
| max_drawdown | 0.9998 |
| cagr | -0.9630 |
| net_avg_win | 8.8038 |
| net_avg_loss | -18.4227 |
| avg_hold_time_bars | 2.6745 |
| exposure | 0.1770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
