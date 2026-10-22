# EMA Hourly Continuation — SSV/USDT P12_200

**Symbol:** SSV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7852 |
| net_win_rate | 0.4801 |
| gross_profit_factor | 0.9185 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -1.2063 |
| sortino_ratio | -0.2850 |
| max_drawdown | 0.3297 |
| cagr | -0.1241 |
| net_avg_win | 78.0923 |
| net_avg_loss | -91.8574 |
| avg_hold_time_bars | 60.6029 |
| exposure | 0.7596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
