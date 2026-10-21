# EMA Hourly Continuation — VET/USDT P34_200

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.8163 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0210 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -1.1535 |
| sortino_ratio | -0.2978 |
| max_drawdown | 0.3560 |
| cagr | -0.1294 |
| net_avg_win | 79.1095 |
| net_avg_loss | -99.9456 |
| avg_hold_time_bars | 32.1846 |
| exposure | 0.4755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
