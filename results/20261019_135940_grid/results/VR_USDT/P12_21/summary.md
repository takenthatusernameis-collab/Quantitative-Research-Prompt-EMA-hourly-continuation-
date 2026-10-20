# EMA Hourly Continuation — VR/USDT P12_21

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1529 |
| net_profit_factor | 0.3285 |
| net_win_rate | 0.2838 |
| gross_profit_factor | 0.6628 |
| gross_win_rate | 0.3159 |
| sharpe_ratio | -20.1487 |
| sortino_ratio | -11.7255 |
| max_drawdown | 1.0000 |
| cagr | -0.9990 |
| net_avg_win | 11.2734 |
| net_avg_loss | -13.6006 |
| avg_hold_time_bars | 2.7443 |
| exposure | 0.1907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
