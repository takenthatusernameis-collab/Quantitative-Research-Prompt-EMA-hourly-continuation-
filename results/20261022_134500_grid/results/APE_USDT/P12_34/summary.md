# EMA Hourly Continuation — APE/USDT P12_34

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1316 |
| net_profit_factor | 0.4009 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8038 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -9.4991 |
| sortino_ratio | -4.8428 |
| max_drawdown | 0.9978 |
| cagr | -0.9090 |
| net_avg_win | 11.8567 |
| net_avg_loss | -22.1128 |
| avg_hold_time_bars | 3.6847 |
| exposure | 0.2204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
