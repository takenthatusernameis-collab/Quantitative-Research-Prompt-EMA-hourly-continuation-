# EMA Hourly Continuation — EDU/USDT P20_26

**Symbol:** EDU/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.5499 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8104 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -3.1836 |
| sortino_ratio | -0.8222 |
| max_drawdown | 0.6162 |
| cagr | -0.3159 |
| net_avg_win | 50.5315 |
| net_avg_loss | -76.4871 |
| avg_hold_time_bars | 4.3750 |
| exposure | 0.0649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
