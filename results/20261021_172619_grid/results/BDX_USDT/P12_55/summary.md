# EMA Hourly Continuation — BDX/USDT P12_55

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.4332 |
| net_win_rate | 0.3860 |
| gross_profit_factor | 0.6816 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -6.0344 |
| sortino_ratio | -1.8431 |
| max_drawdown | 0.8939 |
| cagr | -0.5803 |
| net_avg_win | 38.5098 |
| net_avg_loss | -55.8838 |
| avg_hold_time_bars | 9.8070 |
| exposure | 0.2033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
