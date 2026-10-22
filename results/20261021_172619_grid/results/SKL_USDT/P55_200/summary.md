# EMA Hourly Continuation — SKL/USDT P55_200

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.4856 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -1.3076 |
| sortino_ratio | -0.3105 |
| max_drawdown | 0.3697 |
| cagr | -0.1340 |
| net_avg_win | 74.5922 |
| net_avg_loss | -91.6227 |
| avg_hold_time_bars | 31.4424 |
| exposure | 0.3973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
