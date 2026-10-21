# EMA Hourly Continuation — SKY/USDT P8_20

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.6229 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -3.7773 |
| sortino_ratio | -1.3831 |
| max_drawdown | 0.7315 |
| cagr | -0.4680 |
| net_avg_win | 46.4263 |
| net_avg_loss | -70.7016 |
| avg_hold_time_bars | 4.8811 |
| exposure | 0.1443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
