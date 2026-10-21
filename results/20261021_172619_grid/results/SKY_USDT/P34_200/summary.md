# EMA Hourly Continuation — SKY/USDT P34_200

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8487 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5130 |
| sharpe_ratio | -0.9026 |
| sortino_ratio | -0.2351 |
| max_drawdown | 0.3567 |
| cagr | -0.1045 |
| net_avg_win | 82.2045 |
| net_avg_loss | -102.0330 |
| avg_hold_time_bars | 31.5688 |
| exposure | 0.4735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
