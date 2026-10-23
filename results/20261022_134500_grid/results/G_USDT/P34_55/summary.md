# EMA Hourly Continuation — G/USDT P34_55

**Symbol:** G/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5013 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 1.0177 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -6.7341 |
| sortino_ratio | -2.6867 |
| max_drawdown | 0.9409 |
| cagr | -0.7283 |
| net_avg_win | 30.2164 |
| net_avg_loss | -51.5483 |
| avg_hold_time_bars | 4.9529 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
