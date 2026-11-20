# EMA Hourly Continuation — P2P/USDT P20_200

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.5909 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7518 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -3.4289 |
| sortino_ratio | -0.9873 |
| max_drawdown | 0.7072 |
| cagr | -0.3754 |
| net_avg_win | 55.9472 |
| net_avg_loss | -69.4572 |
| avg_hold_time_bars | 29.8085 |
| exposure | 0.5731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
