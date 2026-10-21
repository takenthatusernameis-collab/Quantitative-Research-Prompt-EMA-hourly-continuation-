# EMA Hourly Continuation — ETHFI/USDT P21_34

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7333 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9482 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.6889 |
| sortino_ratio | -0.4156 |
| max_drawdown | 0.3920 |
| cagr | -0.1739 |
| net_avg_win | 72.7394 |
| net_avg_loss | -93.9775 |
| avg_hold_time_bars | 6.3378 |
| exposure | 0.0853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
