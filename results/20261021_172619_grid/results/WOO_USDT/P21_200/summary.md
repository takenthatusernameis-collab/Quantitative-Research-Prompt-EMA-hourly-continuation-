# EMA Hourly Continuation — WOO/USDT P21_200

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.9290 |
| net_win_rate | 0.5250 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5286 |
| sharpe_ratio | -0.3509 |
| sortino_ratio | -0.0845 |
| max_drawdown | 0.2003 |
| cagr | -0.0416 |
| net_avg_win | 90.0698 |
| net_avg_loss | -107.1628 |
| avg_hold_time_bars | 51.1500 |
| exposure | 0.6510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
