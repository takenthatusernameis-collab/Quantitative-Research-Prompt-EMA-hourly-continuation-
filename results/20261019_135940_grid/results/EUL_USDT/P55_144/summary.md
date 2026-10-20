# EMA Hourly Continuation — EUL/USDT P55_144

**Symbol:** EUL/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.4680 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.7065 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -4.6199 |
| sortino_ratio | -1.3992 |
| max_drawdown | 0.8158 |
| cagr | -0.4843 |
| net_avg_win | 37.1353 |
| net_avg_loss | -57.0577 |
| avg_hold_time_bars | 10.1394 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
