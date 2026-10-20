# EMA Hourly Continuation — VR/USDT P34_200

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.4670 |
| net_win_rate | 0.3288 |
| gross_profit_factor | 0.6856 |
| gross_win_rate | 0.3404 |
| sharpe_ratio | -8.6751 |
| sortino_ratio | -2.7473 |
| max_drawdown | 0.9815 |
| cagr | -0.7935 |
| net_avg_win | 50.2540 |
| net_avg_loss | -52.7306 |
| avg_hold_time_bars | 20.6404 |
| exposure | 0.4879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
