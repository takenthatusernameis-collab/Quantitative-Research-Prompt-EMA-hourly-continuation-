# EMA Hourly Continuation — SSV/USDT P55_200

**Symbol:** SSV/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7191 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -1.8805 |
| sortino_ratio | -0.4874 |
| max_drawdown | 0.4479 |
| cagr | -0.2004 |
| net_avg_win | 69.8708 |
| net_avg_loss | -87.2257 |
| avg_hold_time_bars | 23.5389 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
