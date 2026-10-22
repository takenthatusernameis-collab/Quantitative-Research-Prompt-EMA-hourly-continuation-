# EMA Hourly Continuation — TRX/USDT P21_89

**Symbol:** TRX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.3194 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -9.2144 |
| sortino_ratio | -3.3669 |
| max_drawdown | 0.9897 |
| cagr | -0.8382 |
| net_avg_win | 17.1360 |
| net_avg_loss | -37.6703 |
| avg_hold_time_bars | 11.2846 |
| exposure | 0.3370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
