# EMA Hourly Continuation — SKL/USDT P55_144

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.8159 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -1.1898 |
| sortino_ratio | -0.3150 |
| max_drawdown | 0.3752 |
| cagr | -0.1361 |
| net_avg_win | 79.2212 |
| net_avg_loss | -98.2402 |
| avg_hold_time_bars | 18.4678 |
| exposure | 0.2871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
