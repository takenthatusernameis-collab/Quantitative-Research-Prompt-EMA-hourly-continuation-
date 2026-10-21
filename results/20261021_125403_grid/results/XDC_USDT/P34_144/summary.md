# EMA Hourly Continuation — XDC/USDT P34_144

**Symbol:** XDC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6757 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.2209 |
| sortino_ratio | -0.6227 |
| max_drawdown | 0.5269 |
| cagr | -0.2491 |
| net_avg_win | 56.2454 |
| net_avg_loss | -81.1095 |
| avg_hold_time_bars | 18.0597 |
| exposure | 0.3160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
