# EMA Hourly Continuation — QNT/USDT P12_100

**Symbol:** QNT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 844 |
| net_profit_factor | 0.5774 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9417 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -4.9808 |
| sortino_ratio | -2.0467 |
| max_drawdown | 0.9161 |
| cagr | -0.6224 |
| net_avg_win | 30.9687 |
| net_avg_loss | -49.0106 |
| avg_hold_time_bars | 13.2038 |
| exposure | 0.5065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
