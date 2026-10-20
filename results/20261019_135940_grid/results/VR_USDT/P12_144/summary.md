# EMA Hourly Continuation — VR/USDT P12_144

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.4652 |
| net_win_rate | 0.3416 |
| gross_profit_factor | 0.6929 |
| gross_win_rate | 0.3555 |
| sharpe_ratio | -9.1898 |
| sortino_ratio | -3.2417 |
| max_drawdown | 0.9899 |
| cagr | -0.8395 |
| net_avg_win | 38.9584 |
| net_avg_loss | -43.4479 |
| avg_hold_time_bars | 21.1793 |
| exposure | 0.6229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
