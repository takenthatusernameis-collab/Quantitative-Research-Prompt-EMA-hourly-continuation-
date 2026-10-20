# EMA Hourly Continuation — YFI/USDT P26_34

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.1865 |
| net_win_rate | 0.3507 |
| gross_profit_factor | 0.8232 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -15.3608 |
| sortino_ratio | -7.8884 |
| max_drawdown | 1.0000 |
| cagr | -0.9851 |
| net_avg_win | 5.4189 |
| net_avg_loss | -15.6985 |
| avg_hold_time_bars | 2.3242 |
| exposure | 0.1268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
