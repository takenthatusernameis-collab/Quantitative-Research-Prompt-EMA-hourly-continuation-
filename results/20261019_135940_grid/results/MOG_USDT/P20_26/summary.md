# EMA Hourly Continuation — MOG/USDT P20_26

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1101 |
| net_profit_factor | 0.4881 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.8438 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -10.4113 |
| sortino_ratio | -5.1130 |
| max_drawdown | 0.9975 |
| cagr | -0.9258 |
| net_avg_win | 20.4946 |
| net_avg_loss | -30.5871 |
| avg_hold_time_bars | 2.2071 |
| exposure | 0.1208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
